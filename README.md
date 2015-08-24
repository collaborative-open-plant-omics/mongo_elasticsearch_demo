# mongo_elasticsearch_demo
Demonstration of how to integrate mongodb and elastic search 

- install elasticsearch version 1.4.2

- install mongodb 3.0.5
    - make sure mongodb in running in replicaset mode
        - add --replset "<name>"
        - go to mongo console and type 'rs.intiate()'
            - if you need to change the name of the replica set, it is necesary to delete the .local database from the mongodb instance

- install elasticsearch mongoriver and mapper attachments (go to github to check versions....these can be problematic):
    - $ bin/plugin --install com.github.richardwilly98.elasticsearch/elasticsearch-river-mongodb/2.0.0
    - $ bin/plugin --install elasticsearch/elasticsearch-mapper-attachments/2.0.0.RC1

- setup mongoriver by running commands in mongo_river_setup.txt

