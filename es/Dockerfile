FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.3.0
COPY --chown=elasticsearch:elasticsearch backup /backup
RUN chmod -R 775 /backup
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config
USER elasticsearch
EXPOSE 9200

