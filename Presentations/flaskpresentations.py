#postman used for testing web applications 
# https://www.postman.com

#flask is a web framework for python
#choose a location, open new folder called flask and file called app.py

#REST - creating an API
#add an API
    #client server architecture
    #statelesness
    #cacheability
    #layered system
    #uniform interface
        #providing a unifrm interace simplfies application architecture, and decouples components of the system
        #if our API is trult RESTful, a client shouldnt have to know anything about how an API is implemented in order to start making requests and utilizing the responses
        #Richardson maturity level
            #describes four levels of conformity with REST Principles
            #should be aiming for level 2/3
            #1 THE SWAMP OF POX, 2 RESOURCES, 3 HTTP VERBS,4 HYPERMEDIA CONTROLS
            #Resources
                #are the entities, be they documents, files, database records or other bits of data, that your application works with
            #HTTP Verbs
                #http request is made using a speciifc "method" and each method is expected to produce different behavior 
                #commonly used HTTP methods include GET, POST, PATCH and DELETE. We can map these methods directly to the CRUD(create, read, update and delete) operations
            #Hypermedia Controls(DONT NEED, BUT GOOD STRETCH TARGET)
                #HATEOAS links - highest level of conformity to rest principles, an API should use hypermedia controls
#Flask dependencies
    #flask: the core flask library
    #mysqlclient: a database driver for MYSQL server
    #flask-SQLAlchemy: an interface between MYSQL and Python
    #flask-marshmallow: an object serialiser; and 
    #marshmallow - sqlalchemy: integration for the above libraries

#Project - think about something to create and create an api based on this
#modular programs are generally easier to read, test

#flask configuration

