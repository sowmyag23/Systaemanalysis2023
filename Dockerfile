FROM python:3
ARG LISTEN_PORT="3333"
ADD helloworld.py /
RUN pip install flask
EXPOSE ${LISTEN_PORT}
ENTRYPOINT [ "python" ]
CMD [ "helloworld.py" ]
