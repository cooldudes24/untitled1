#ALL of code made by Mr.Constantius. Have my little work in a Jupyter Notebook, will publish soon.

import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from urllib.parse import urlsplit
import json

import requests
from bs4 import BeautifulSoup, Tag

# TODO : convert ot threadpool executor based scraper


def scrape_leader(url):
    url_splitted = urlsplit(url)
    base = url_splitted.scheme + "://" + url_splitted.netloc
    raw = requests.get(url)
    soup = BeautifulSoup(raw.content, "html.parser")
    table = soup.find_all("table", {"class": "wikitable"})
    leaders = []
    for t in table:
        tbody = t.find("tbody")
        g_i = vg_i = None
        current = ""
        # cognitive complexity isn't good here ( too many if and else ), don't use this as the best example
        for tr in tbody:
            if type(tr) is Tag:
                # get gov and vice gov column by header index
                ths = tr.find_all("th")
                if len(ths) > 1:
                    # should be handle for another header name like Bupati or Wakil Bupati
                    for i, th in enumerate(ths, start=0):
                        if th.text.strip() in ["Kepala Daerah", "Bupati", "Wali kota", "Bupati/Wali Kota"]:
                            g_i = i
                            current = th.text.strip() if th.text.strip() != "Kepala Daerah" else ""
                            if th.has_attr("colspan"):
                                g_i += 1
                        if th.text.strip() in ["Wakil Kepala Daerah", "Wakil Bupati", "Wakil Wali kota",
                                               "Wakil Bupati/Wali Kota"]:
                            vg_i = i
                            if th.has_attr("colspan"):
                                vg_i += 2
                if g_i == None or vg_i == None:
                    continue  # case Riau
                if g_i == vg_i:
                    vg_i = vg_i + 1  # case bupati/walikota has colspan, wakil no colspan, case Maluku

                # skip unused th
                th = tr.find("th")
                if type(th) is not int and th is not None and th.has_attr("colspan"):
                    # ambil Bupati/Wali Kota
                    current = th.text.strip()
                    continue
                if tr.find("th") is not None or ("style" in tr and "display:none" in tr[
                    "style"]):
                    continue
                # scrape table value
                tds = tr.find_all("td")
                if tds:
                    # should be filled with default number, maybe
                    if g_i and vg_i:
                        g = tds[g_i].findChildren("a", recursive=False)
                        g_pic = tds[1].findChildren("img", recursive=True)
                        vg = tds[vg_i].findChildren("a", recursive=False)
                        vg_pic = tds[g_i + 1].findChildren("img", recursive=True)
                        region = tds[0].findChildren("a", recursive=True, class_=lambda x: x != 'image')[0].text

                        if "Kabupaten" not in region and "Kota" not in region:
                            region = "Kabupaten " + region if current == "Bupati" else "Kota " + region  # case Singkawang, Kalimantan Barat & Humbang Hasundutan, Sumatra Utara

                        # check space between Kabupaten/Kota and name
                        if "Kabupaten" in region:
                            region = region[:9] + " " + region[9:] if region[9] != " " else region
                        elif "Kota" in region:
                            region = region[:4] + " " + region[4:] if region[4] != " " else region

                        if g:
                            name = g[0].text
                            if name == "Pj." and g[1]:
                                name = g[1].text
                        else:
                            name = tds[g_i].text.strip()  # case name is text only not link

                        name = "" if name.lower() in ["kosong"] or "lowong" in name.lower() else name
                        if name:
                            leader = {
                                "name": name,
                                "title": "Bupati" if "Kabupaten" in region else "Walikota",
                                "community": region
                            }
                            pic_url = normalize_image_url(g_pic[0]["src"]) if g_pic else ""
                            if pic_url:
                                leader["pic_url"] = pic_url
                            wiki_url = base + g[0]["href"] if g else ""
                            if wiki_url and not "action=edit" in wiki_url:
                                leader["wiki_url"] = wiki_url
                            leaders.append(leader)

                        name = ""
                        if vg:
                            name = vg[0].text
                            if name == "Pj." and vg[1]:
                                name = vg[1].text
                        else:
                            name = tds[vg_i].text.strip()  # case name is text only not link

                        name = "" if name.lower() in ["kosong"] or "lowong" in name.lower() else name
                        if name:
                            leader = {
                                "name": name,
                                "title": "Wakil Bupati" if "Kabupaten" in region else "Wakil Walikota",
                                "community": region
                            }
                            pic_url = normalize_image_url(vg_pic[0]["src"]) if vg_pic else ""
                            if pic_url:
                                leader["pic_url"] = pic_url
                            wiki_url = vg[0]["href"] if vg else ""
                            if wiki_url and not "action=edit" in wiki_url:
                                leader["wiki_url"] = base + wiki_url
                            leaders.append(leader)
    # if not leaders:
    #     print(url, leaders)
    return leaders


def normalize_image_url(url):
    if "GAMBAR_TIDAK_TERSEDIA" in url:
        return ""
    base = url[:url.find("/thumb/")]
    extension = ".jpg" if ".jpg" in url else ".png"
    path = url[url.find("thumb/") + len("thumb"):url.find(extension) + len(
        extension)]
    return "https:" + base + path


def main():
    root_url = "https://id.wikipedia.org/wiki/Kategori:Daftar_bupati_dan_wali_kota_di_Indonesia"
    url_splitted = urlsplit(root_url)
    raw = requests.get(root_url)
    soup = BeautifulSoup(raw.content, "html.parser")
    links = soup.find_all("a", href=re.compile("(.*?Daftar_Kepala_Daerah_dan_Wakil_Kepala_Daerah.*)"))
    # TODO: thread pool here
    leaders = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        for link in links:
            if any(city in link["href"] for city in
                   []):
                # ["Kalimantan_Barat","Maluku","Maluku_Utara"]):
                continue
            futures.append(
                executor.submit(scrape_leader, url=url_splitted.scheme + "://" + url_splitted.netloc + link["href"]))
        for future in as_completed(futures):
            # print(future.result())
            leaders = leaders + future.result()
    # for link in links:
    #     if any(city in link["href"] for city in ["Nusa_Tenggara_Barat", "Sumatra_Utara"]):
    #         continue
    #     print(link)
    #     scrape_leader(url_splitted.scheme + "://" + url_splitted.netloc + link["href"])

    # i commented out the print statement since it'll be too messy if we have so many scrapped data.
    # pprint(leaders)
    with open("result.json", "w+") as result_file:
        json.dump(leaders, result_file, indent=4)
    print("json dumped, leaders size : ", len(leaders))


if __name__ == "__main__":
    main()
