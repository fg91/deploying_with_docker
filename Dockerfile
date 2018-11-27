FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
COPY ./deploying_random_forest/ /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python
RUN pip install -r requirements.txt \
&& python -m nltk.downloader averaged_perceptron_tagger
CMD python expose_rf.py
