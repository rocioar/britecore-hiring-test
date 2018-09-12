
Brite Core Hiring Test frontend
===============================

Frontend for britecore-api that lets you visualize the list of RiskTypes and builds custom forms.

Development Environment
-----------------------

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev
```

Deployment
----------

``` bash
# build for production with minification
npm run build

# install and configure aws-cli with your AWS credentials
pip install awscli
aws configure

npm run deploy <bucket_name>
```

Settings
--------

`ROOT_API`: Indicates the base url for the API, you can set it up on `config/dev.env.js` for development and `config/prod.env.js` for production.
