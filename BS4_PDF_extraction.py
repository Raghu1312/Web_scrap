#!/usr/bin/env python
# coding: utf-8

# In[28]:


pip install beautifulsoup4


# In[29]:


pip install requests


# In[30]:


pip install html5lib


# In[ ]:





# # Without name conversion - Working code 

# In[2]:


import requests
from bs4 import BeautifulSoup
import os

# URL from which pdfs to be downloaded
url = "https://www.careinsurance.com/health-insurance-proposal-forms.html"
save_dir = 'C:\\Users\\Ragha\\Desktop\\web'

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
i = 0

# From all links check for pdf link and
# if present download file
for link in links:
        if ('.pdf' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)

            # Get response object for link
            response = requests.get(link.get('href'))

            # Write content in pdf file     
            pdf = open(os.path.join(save_dir, "pdf"+str(i)+".pdf"), 'wb')
            pdf.write(response.content)
            pdf.close()


# ## Naming coversion - Working code

# In[1]:


import requests
from bs4 import BeautifulSoup
import os
import posixpath
from urllib.parse import urlsplit, unquote


# URL from which pdfs to be downloaded
url = "https://templatesdeal.com/product/new-zealand-passport-template"
save_dir = 'C:\\Users\\JosephKiranAmbrose\\Desktop\\USHUR\\BeautifulSoup4\\BS4_pdf_extraction'

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
i = 0
# From all links check for pdf link and
# if present download file
for link in links:
        if ('.pdf' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)

            # Get response object for link
            response = requests.get(link.get('href'))
            
            #Splitting URL & extracting file name
            url = link.get('href')
            urlpath = urlsplit(url).path
            basename = posixpath.basename(unquote(urlpath))
            

            # Write content in pdf file
            if response.status_code == 200:
                # extract the file name from the URL
                filename = os.path.join(save_dir, basename)

                # write the PDF to a file with the original file name
                with open(filename, 'wb') as f:
                    f.write(response.content)
                    print(f'{filename} downloaded successfully.')


# In[ ]:




