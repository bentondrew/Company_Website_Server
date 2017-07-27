FROM drewantech/flask:2.0.0
MAINTAINER Benton Drew <benton.s.drew@drewantech.com>
USER root
ADD service/ .
USER python_user
