#Dockerfile with basic configurations spelled out

#ARG IMG=python:3.9
#FROM $IMG AS base
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=bitnami/git:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

ARG IMG=continuumio/anaconda3
FROM $IMG
ARG IMG
RUN echo "...installed $IMG"

#ARG IMG=hasicorp/terraform:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=amazon/aws-cli:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=mcr.microsoft.com/azure-cli:latest
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"

#ARG IMG=gcr.io/google.com/cloudsdktool/google-cloud-cli:410.0.0
#FROM $IMG
#ARG IMG
#RUN echo "...installed $IMG"


#########################################
#- Ensure everything is up to date
#########################################
RUN apt-get update -y

#########################################
#- Install VIM
#########################################
ARG PACKAGES=vim
RUN apt-get install ${PACKAGES} -y

#########################################
#- Install libraries for Python needs
#########################################
ARG PACKAGES=libgeos-dev
RUN apt-get install ${PACKAGES} -y

#########################################
#- Final clean-up
#########################################
RUN apt-get clean -y

CMD ["rm", "-rf", "/var/lib/apt/lists/*"]

