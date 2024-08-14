FROM python:3.11-alpine


COPY ./ /engbobr
WORKDIR /engbobr
RUN python -m pip install -r requirements.txt
RUN groupadd -r user && useradd -g user user
RUN chown -R user:user /engbobr
USER user
EXPOSE 27000
CMD ["sh", "-c", "python3 main.py"]