# Subdomain-Toolkit
This tool combines 5 different subdomain discovery tools. Then it filters the strings that are the same. And finally, it filters only subdomains that give 200 OK responses.


---

## 1. Installation

```
git clone https://github.com/Mr0Wido/Subdomain-Toolkit.git
cd Subdomain-Toolkit
sudo python3 setup.py install
```

## 2. Manuel Installation

Install subfinder, assetfinder, amass and sublist3r
```
sudo apt-get install subfinder assetfinder amass sublist3r
```

Install findomain
```
curl -LO https://github.com/findomain/findomain/releases/latest/download/findomain-linux.zip
unzip findomain-linux.zip
chmod +x findomain
sudo mv findomain /usr/bin/findomain
```

Install Subdomain-Toolkit
```
git clone https://github.com/Mr0Wido/Subdomain-Toolkit.git
cd Subdomain-Toolkit
sudo cp subdomain.py /usr/bin/subdomain
chmod +x subdomain
```

## 3. Usage

```
subdomain -u <target-domain>
```

https://user-images.githubusercontent.com/88449391/227714949-b3289792-926a-4f31-af8a-bc6ddc6e2825.mp4




