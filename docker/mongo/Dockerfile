# This is a docker file for create a ubuntu image with mongodb 
# 
#
#

# Set a father image
FROM sshd

# Set the maintainer information
MAINTAINER from ubuntu by welion (353566165@qq.com)


#Install mongodb & pwgen
RUN apt-get update
RUN apt-get install -y mongodb pwgen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    
#创建mongodb存放数据的文件夹
RUN mkdir -p /data/db
RUN chown mongodb:mongodb /data/db
VOLUME /data/db
RUN sed -i 's/dbpath=\/var\/lib\/mongodb/dbpath=\/data\/db/g' /etc/mongodb.conf
RUN sed -i 's/bind_ip = 127.0.0.1/bind_ip = 0.0.0.0/g' /etc/mongodb.conf

ENV AUTH no

#添加脚本
ADD run.sh /run.sh
ADD set_mongodb_password.sh /set_mongodb_password.sh
RUN chmod 755 ./*.sh

EXPOSE 27017
EXPOSE 27018


# Set the init command
CMD ["/run.sh"]
