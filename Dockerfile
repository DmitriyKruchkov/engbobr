FROM python:3.11-alpine


COPY ./ /engbobr
RUN python -m pip install -r requirements.txt
WORKDIR engbobr
USER user
CMD ["sh", "-c", "python main.py"]