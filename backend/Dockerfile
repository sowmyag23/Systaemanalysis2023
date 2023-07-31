FROM python:3
ADD backend.py /
RUN pip install pymongo requests
EXPOSE ${LISTEN_PORT}
ENTRYPOINT [ "python" ]
CMD [ "backend.py" ]
