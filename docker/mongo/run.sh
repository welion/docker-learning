#!/bin/bash

if [ ! -f /data/db/mongod.lock ]; then
   /usr/bin/mongod --config /etc/mongodb.conf
else
    export mongodb=$mongodb' --dbpath /data/db'
    rm /data/db/mongod.lock
    mongod --dbpath /data/db --repair && /usr/bin/mongod --config /etc/mongodb.conf
fi