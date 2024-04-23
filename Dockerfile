FROM python
WORKDIR /test
COPY . /test
RUN pip install nltk
RUN python -m nltk.downloader stopwords
CMD [ "python","app.py"]