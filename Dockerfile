FROM python:3.12-rc-bullseye
# alpine è abbastanza minimale da richiedere 10 minuti per installare il minimo indispensabile
# (grazie mille cffi, grazie mille gcc, e MIO DIO GRAZIE CLANG E LLVM, vi adoro tutti)
# e dopo la terza volta che mi parte la build perchè pip non si sa installare le dependency
# da solo, non mi mette l'apk add nell acache, e mentre mi finisce tutta la mattinata davanti
# a questo dannatissimo terminale, direi che, caro mio, vatti a benedire dal soffitto

# postgres install:
# visto che railway non supporta docker-compose postgres va aggiunto a mano
# per adesso faccio il deploy con sqlite, vedo poi come/se riesco a mettere postgres
# che la cosa non sta finendo bene
# visto che postgres non si riesce a metterlo per adesso neanche psy... quello
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# python
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY ./ecom/ /code/

# https://docs.docker.com/engine/reference/builder/
# port
EXPOSE 8000
# run container
CMD [ "python3", "/code/manage.py", "runserver" ]

