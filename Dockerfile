FROM python:3
ARG LISTEN_PORT="3333"
ADD frontend.py /
RUN pip install flask pymongo
EXPOSE ${LISTEN_PORT}
ENTRYPOINT [ "python" ]
CMD [ "frontend.py" ]
