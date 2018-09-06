Brite Core Hiring Test Project
==============================

This is a solution for the [ProductDevelopment project](https://github.com/IntuitiveWebSolutions/ProductDevelopmentProject) proposed by BriteCore.

It is divided in two parts:

* Backend: built with Django and Django Rest Framework, CRUD API that lets you manage the RiskTypes and the Fields for those Risks Types.
* Frontend: static site built with VueJS which uses the backend to query for Risks Types and their field forms

Deployment
----------

The backend was deployed using AWS Lambda and Zappa under:

* [britecoreapi.schegel.net](https://britecoreapi.schegel.net)


The frontend was deployed on an S3 bucket and the url to access it is:

* [britecore.schegel.net](http://britecore.schegel.net)

