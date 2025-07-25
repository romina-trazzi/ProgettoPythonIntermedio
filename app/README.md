
## Funzionalità Principali

- **Analisi del Sentiment**: Analizza il sentiment di recensioni di prodotti (positivo, negativo, neutro).
- **Sistema di Raccomandazione**: Fornisce raccomandazioni di prodotti basate sulle interazioni degli utenti.
- **Analisi dei Dati**: Visualizza statistiche e insight sui dati di prodotti, utenti e recensioni.


## Installazione

1.  **Clona il repository**:
    ```bash
    git clone <URL_DEL_REPOSITORY>
    cd ProgettoPythonIntermedio
    ```

2.  **Crea e attiva un ambiente virtuale** (raccomandato):
    ```bash
    python -m venv venv
    # Su Windows
    .\venv\Scripts\activate
    # Su macOS/Linux
    source venv/bin/activate
    ```

3.  **Installa le dipendenze**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inizializza il database**:
    ```bash
    python db/init_db.py
    ```

## Esecuzione dell'Applicazione

Per avviare l'applicazione FastAPI:

```bash
# Assicurati di essere nell'ambiente virtuale attivato
uvicorn app.main:app --reload
```

L'applicazione sarà disponibile all'indirizzo `http://127.0.0.1:8000/`.
La documentazione interattiva è accessibile su `/docs` (Swagger UI) e `/redoc` (ReDoc).

## Esecuzione dei Test

Per eseguire i test unitari:

```bash
# Assicurati di essere nell'ambiente virtuale attivato
python -m unittest discover tests
```


## Tecnologie Utilizzate

- Python
- FastAPI
- SQLAlchemy
- scikit-learn
- NLTK
- Pandas
- NumPy
- HTML/CSS/JavaScript

## Contribuzione

Sentiti libero di contribuire al progetto. Si prega di seguire le linee guida di contribuzione (se presenti).

## Licenza


Questo progetto è rilasciato sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

# ProgettoPythonIntermedio

Questo è un progetto Python intermedio che implementa un sistema di analisi del sentiment e raccomandazione di prodotti, con funzionalità di analisi dei dati.

## Struttura del Progetto

```
app/
    main.py
    models/
        product.py
        purchase.py
        review.py
        user.py
    services/
        data_service.py
        recommendation_service.py
        sentimentt_service.py
    views/
        api_routes.py
        web_routes.py
    db/
        init_db.py
    utils/
        database.py
    static/
        ...
    templates/
        ...
    tests/
        test_data_analysis.py
        ...
Readme.md
requirements.txt
```