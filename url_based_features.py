import re
class url_based_features():
    def __init__(self,URL):
        self.URL = URL

    #has_ip
    def contains_ip(self):
        if re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",self.URL):
            return 1
        else:
            return -1


    #has @ in address
    def at_exists(self):
        if not re.findall("@",self.URL):
            return -1
        return 1

    #has_many_dots
    def dot_count(self):
        if re.findall('//',self.URL):
            sub_domain_tld = self.URL.split("://")[1].split('/')[0]
        else:
            sub_domain_tld = self.URL.split('/')[0]
        rest_of_url = sub_domain_tld.split(".")
        if (len(rest_of_url) == 3 or len(rest_of_url) == 2 ) :
            return -1
        if (len(rest_of_url) == 4) :
           return  0
        else:
           return 1


    #existing_https_token
    def exisiting_https_token(self):
        if re.findall("http://https",self.URL):
            return 1
        else :
            return -1

    #existing_suffix_prefix
    def suffix_prefix_exists(self):
        _,domain,_ = self.extract_domain(self.URL)
        if re.search("-",domain):
            return 1
        return -1

    #URL length indicator
    def url_length(self):
        if len(self.URL) <54:
            return -1
        if len(self.URL)>54 and len(self.URL)<75 :
            return 0
        else :
            return 1
    #is_url shortened
    def is_URL_shortened(self):
      match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                  'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                  'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                  'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                  'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                  'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                  'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net', self.URL)
      if match:
        return 1
      else:
        return -1

    #redirection
    def redirecting(self):
        list_ = re.findall("//",self.URL)
        if len(list_)>1:
            return 1
        return 1

    #extract domain
    def extract_domain(self,URL):
        if self.contains_ip():
          return '','no_domain',''
        #remùoving https/http and directory
        if re.findall("://",URL):
            sub_domain_and_top_domain = URL.split("//")[-1].split('/')[0]#split https ou domain
        else:
            sub_domain_and_top_domain = URL.split('/')[0]
        #splitting sub/domain/tld
        split = sub_domain_and_top_domain.split('.')
        if len(split) == 3 :
          return split[0], split[1], split[2]
        if len(split) == 2 :
          return 'www',split[0],split[1]

        #general case
        top_domains = []
        domain = ''
        sub_domains = []

        try:

          if len(split[-1])<4 and len(split[-2])<4:
              top_domains.append(split[-2])
              top_domains.append(split[-1])
              domain = split[-3]
              sub_domains = split[:-3].copy()

              return sub_domains,domain,top_domains
          if len(split[-1])<5:
              top_domains.append(split[-1])
              domain = split[-2]
              sub_domains = split[:-2].copy()

        except:
          print("error in extarcting domain")
        if not domain:
          domain = 'not found'
        if not sub_domains:
          sub_domains = ''
        if not top_domains:
          top_domains = ''
        return sub_domains,domain,top_domains


        #returning a vector containing the results
    def result_url(self):
        result = []
        result.append(self.contains_ip())
        result.append(self.url_length())
        result.append(self.is_URL_shortened())
        result.append(self.at_exists())
        result.append(self.redirecting())
        result.append(self.suffix_prefix_exists())
        result.append(self.dot_count())
        result.append(self.exisiting_https_token())




        return result
