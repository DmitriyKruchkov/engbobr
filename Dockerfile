FROM python:3.11-alpine


COPY ./ /engbobr
WORKDIR /engbobr
RUN python -m pip install -r requirements.txt
USER user
CMD ["sh", "-c", "python3 main.py"]