import whois
# python-whois (check online doc)
from url_based_features import url_based_features
from domain_based_features import domain_based
from html_based_features import html_based
import pandas as pd
all_in = []
#it is recommended that the url be in a standard format
df = pd.read_csv('dataset_url.csv',header=0,
                 names=['Domain','Open Page Rank'])
list_of_url = list(df['Domain'])
print("The first 100 url form the dataset")
print(list_of_url[:100])
for URL in list_of_url:
    print("https://"+URL.lower())

    a = url_based_features("https://"+URL.lower())

    IP,url_length,shortened,redirect,at,sufi_pref,dot,https = a.result_url()
    print(" Ip =",IP,"\n","@= ",at,"\n","dot =",dot,"\n","https token =",
          https,"\n","sufi_pref = ",sufi_pref,"\n","url_length",url_length,"\n",
          "shortened =",shortened,"\n","redirection =",redirect)
    b = domain_based("https://"+URL.lower())
    page_score,google_index,rank_page,non_standard_port,ssl, domain_life,\
    abnormal_url,domain_age, dns_record = b.result_domain()
    print("is url abnormal",abnormal_url)
    print("domain life",domain_life)
    print("domain age",domain_age)
    print("ranking",rank_page)
    print("google index",google_index)
    print("page score",page_score)
    print("SSL",ssl)
    print("non standard port", non_standard_port)
    print("DNS_record",dns_record)

    c = html_based("https://"+URL.lower())
    favicon,url_of_anchor,confermity,SFH,mailto,forwarding,on_mouseover,\
    right_click,pop_up,iframe,links_pointing=c.results_html()
    print("iframe",iframe)
    print("favicon",favicon)
    print("confermitry",confermity)
    print("mailto = ",mailto)
    print("on_mouseOver",on_mouseover)
    print("right click",right_click)
    print("forwarding", forwarding)
    print("SFH",SFH)
    print("links",links_pointing)
    print("url_anchor",url_of_anchor)
    print("popup",pop_up)

    final_output = [IP,url_length,shortened,at,redirect,dot,sufi_pref,ssl,
                    domain_life,favicon,non_standard_port,https,confermity,
                    url_of_anchor,confermity,SFH,mailto,abnormal_url,forwarding,on_mouseover,
                    right_click,pop_up,
                    iframe,domain_age,dns_record,rank_page,page_score,google_index,links_pointing
                    ]
    print(final_output)
    all_in.append(["https://"+URL]+final_output)
df_final = pd.DataFrame(data=all_in)
df_final.to_csv("test.csv")
