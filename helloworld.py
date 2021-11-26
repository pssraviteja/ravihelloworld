#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "hello worlds"

if __name__=="__main__":
    app.run()

