# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
#ARG VARIANT=3-bullseye
ARG RELEASE_VERSION=3.9
FROM python:${RELEASE_VERSION}

ARG RELEASE_VERSION=latest
FROM bitnami/git:${RELEASE_VERSION}
FROM node:${RELEASE_VERSION}
FROM continuumio/anaconda3
FROM hashicorp/terraform:${RELEASE_VERSION}
FROM amazon/aws-cli:${RELEASE_VERSION}
FROM mcr.microsoft.com/azure-cli:${RELEASE_VERSION}
#FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:${RELEASE_VERSION}
FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:410.0.0

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
