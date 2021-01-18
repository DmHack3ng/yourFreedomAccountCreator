
import requests
import subprocess
from BeautifulSoup import BeautifulSoup 
import urlparse
import subprocess,os, time
import re 
 

session=requests.Session()

mail_url="https://mohmal.com/en/inbox"
filename="securimage_show.jpg" 
image_link="https://www.your-freedom.net/securimage/securimage_show.php" 
furl="https://www.your-freedom.net/index.php?id=register"
payload_url="https://www.mohmal.com/en/message/" 
test_url="https://www.your-freedom.net/index.php?id=171&username=Dmthote&auth=096688fc&submit=Activate+account" 
ref_url="https://www.your-freedom.net/index.php?id=171"
comp_url="http://www.your-freedom.net/index.php?id=171&username=Dmthoste&auth=cd7ac05c&submit=Activate+Account"

def run_limCreator():
    print("\n[++] Sending Data to Server ")
    init_data_account(furl)
    dat=connect_to_mailsite(mail_url)
    get_confirm_mail(dat)
	

def download_image(link):
    data=session.get(link)
    with open("securimage_show.jpg","wb") as yop:
        yop.write(data.content)
    time.sleep(7)    
    print("=> Captcha Image Downloaded" ) 
    subprocess.call("termux-open " +filename,shell=True)
    time.sleep(8)
    os.remove(filename)
    
def connect_to_mailsite(url):
    #time.sleep(10) 
    get_mail_site=session.get(url)
    return get_mail_site.content

def dissecting_mail(html_page):
    yo=BeautifulSoup(html_page)
    all_div=yo.findAll("div")
    for div in all_div:
        id=div.get("data-email")
        if id:
            return str(id) 
                
def get_captcha_code():
	 code = raw_input("[+] Valeur de l'image >> ")
	 return code 

        
def actual_mail():
    data=connect_to_mailsite(mail_url)
    mail=dissecting_mail(data)
    print("\nMail => " + mail +"\n")
    
def get_confirm_mail(html_code):
    if "User Registration" in str(html_code):
        print("\r[ ++ ] New Mail ..Reading ")
        number=get_msg_id(html_code)
        print("\nMsg ID =>" +number) 
        get_payload_url=payload_url+number
        ultime_payload=session.get(get_payload_url)
        ult_link=get_ultime_link(ultime_payload.content) 
        test_url=ult_link 
        time.sleep(6)
        ending_post(test_url,ref_url)
    else: 
        print("\rWaiting Mail :) ...Refreshing ")
        time.sleep(6)
        html_c=connect_to_mailsite(mail_url)
        get_confirm_mail(html_c)

		
def write_report(data, name):
    with open(name, "w" ) as ze:
        ze.write(str(data))
def check_report(filename):
    with open(filename,"r") as tz:
        return tz.read()
        tz.close() 

def finder(filename,character):
    with open(filename,"r") as prod:
        file_content=prod.read()
        soup=BeautifulSoup(file_content)
        search_result=soup.findAll(character)
        for char in search_result:
            return char
            
def finderv2(data_code, character):
    soup=BeautifulSoup(data_code)
    search_result=soup.findAll(character)
    return search_result    
          
def get_msg_id(code_html):
    result=finderv2(str(code_html),"tbody") 
    reend=re.findall("id=.\d*", str(result))[0] 
    get_id=reend.split('"')[1]
    return get_id

    
def get_ultime_link(payload):
    return  str(re.search("http://www.your-freedom.net/\D*id=\d*&username=\w*&auth=\w*&L=\d", payload).group(0)+"&submit=Activate+Account")

def define_data(url):
    get_username=url.split("&")[1].split("=")[1]
    get_authcode=url.split("&")[2].split("=")[1]
    return get_username , get_authcode
    
def ending_post(end_url,ref_page):
    end_url=re.sub("&L=\d","",end_url)
    print("\nFinal Payload =>" +end_url)
    user,auth=define_data(end_url)
    gang=session.get(ref_page)
    form=finderv2(str(gang.content),"input")
    for res in form:
        post_dat={}
        name=res.get("name")
        value=res.get("value")
        if name=="username":
            value=user
            print(user)
        elif name=="authcode":
            value=auth
            print(auth)
        post_dat[name]=value
    az=session.post(end_url,data=post_dat) 
    write_report(az.content,"end_session.html")
    show_account_report(user)
    	 
def init_data_account(url):
        data=session.get(url)
        beauty=BeautifulSoup(data.content)
        all_form=beauty.findAll("form")
        for form in all_form:
            method =form.get("method") 
            action=form.get("action")
            post_url=urlparse.urljoin(url,action)
            post_data={}
            all_input=form.findAll("input")
            method=form.get("method")
            #print(post_url)
            All_input =form.findAll("input")
            #print(action) 
            for input in all_input :
                #print(input)
                value =input.get("value")
                name=input.get("name")
                type=input.get("type")
                if name =="username":
                    value="Dmthozrste" 
                elif name=="password":
                    value ="DZOUMOGNE976" 
                elif name =="repeat":
                    value ="DZOUMOGNE976" 
                elif type=="checkbox":
                    value ="on" 
                elif name=="email":
                    #print(input) 
                    data=connect_to_mailsite(mail_url)
                    mail=dissecting_mail(data)
                    value=mail
                    print(value)
                elif name=="captcha_code":
                    download_image(image_link)
                    value=get_captcha_code()
                    #print(value) 
                post_data[name]=value
            dm=session.post(post_url,data=post_data)
            #print(dm.content)
            write_report(str(dm.content),"rapport.html") 
            #time.sleep(5)
            report_content=check_report("rapport.html")
            if "User Registration" in report_content:
                print("[+] Successully Send it ...Connecting Mail")
            else:
                print("[-] Failed to send data of Server") 

def show_account_report(user):
    print("\n[+] Your Account Has Created Successfully\n")
    print("############ Account Details ############")
    print("\nUsername => "+user)
    print("\nPassword => DZOUMOGNE976")
    print(actual_mail())
               

def get_account_nb(file):
    new_list=[]
    da=check_report(file)
    actual_v=da.split(",")
    print(actual_v)    
    for v in actual_v :
        nb=int(v)
        nb=nb+2
        new_list.append(nb)
    new_list[0]+=1
    new_list[1]+=1
    new_list[2]+=1
    print(new_list)
    write_report(new_list, "zo.txt") 

#ending_post(comp_url, ref_url)         
#get_account_nb("zo.txt")
run_limCreator()


