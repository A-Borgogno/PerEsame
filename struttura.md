# Struttura del Database Formula 1 (Basato su Ergast API)

Questo documento analizza la struttura del database relazionale di Formula 1, originariamente fornito dalla Ergast Developer API. Lo schema è progettato per immagazzinare in modo efficiente e coerente decenni di dati storici.

---

### 1. Tabelle Anagrafiche (I "Protagonisti" del Database)

Queste tabelle contengono le informazioni di base e le entità principali che non cambiano frequentemente.

#### `seasons` (Stagioni)
Contiene l'elenco di tutti gli anni di campionato presenti nel database.
* `year`: L'anno della stagione (es. 2023). Funge da chiave primaria.

#### `circuits` (Circuiti)
Elenco e dettagli di tutti i circuiti.
* `circuitId`: Identificatore numerico unico per ogni circuito (chiave primaria).
* `circuitRef`: Riferimento testuale breve e unico (es. `monaco`, `silverstone`).
* `name`: Nome completo del circuito (es. "Circuit de Monaco").
* `location`: Città o località del circuito.
* `country`: Nazione del circuito.
* `lat`, `lng`: Coordinate geografiche (latitudine e longitudine).
* `alt`: Altitudine sul livello del mare.
* `url`: Link (solitamente Wikipedia) con maggiori informazioni.

#### `drivers` (Piloti)
Dati anagrafici di tutti i piloti.
* `driverId`: Identificatore numerico unico per ogni pilota (chiave primaria).
* `driverRef`: Riferimento testuale unico (es. `hamilton`, `vettel`).
* `number`: Numero di gara permanente del pilota (es. 44).
* `code`: Codice di tre lettere usato in TV (es. "HAM", "VET").
* `forename`: Nome di battesimo.
* `surname`: Cognome.
* `dob`: Data di nascita (Date Of Birth).
* `nationality`: Nazionalità del pilota.
* `url`: Link alla pagina Wikipedia del pilota.

#### `constructors` (Costruttori/Scuderie)
Dati di tutte le scuderie.
* `constructorId`: Identificatore numerico unico (chiave primaria).
* `constructorRef`: Riferimento testuale unico (es. `mercedes`, `ferrari`).
* `name`: Nome completo della scuderia.
* `nationality`: Nazionalità della scuderia (basata sulla licenza).
* `url`: Link alla pagina Wikipedia della scuderia.

#### `status` (Stati di Fine Gara)
Tabella di servizio che descrive lo stato finale di un pilota in una gara.
* `statusId`: Identificatore numerico unico (chiave primaria).
* `status`: Descrizione testuale (es. "Finished", "+1 Lap", "Engine", "Collision").

---

### 2. Tabella Centrale degli Eventi

Questa tabella definisce ogni singolo evento (Gran Premio).

#### `races` (Gare)
* `raceId`: Identificatore numerico unico per ogni gara (chiave primaria).
* `year`: Anno della gara (collega a `seasons`).
* `round`: Numero della gara all'interno della stagione.
* `circuitId`: ID del circuito. **Chiave esterna** che collega a `circuits.circuitId`.
* `name`: Nome ufficiale del Gran Premio (es. "Monaco Grand Prix").
* `date`: Data esatta della gara.
* `time`: Ora di inizio della gara.
* `url`: Link alla pagina Wikipedia di quella specifica edizione.

---

### 3. Tabelle di Risultati e Performance

Queste tabelle registrano i dati "dinamici" del weekend di gara.

#### `results` (Risultati di Gara)
Risultati finali di ogni pilota per ogni gara.
* `resultId`: ID unico del risultato (chiave primaria).
* `raceId`: Collega alla gara in `races`.
* `driverId`: Collega al pilota in `drivers`.
* `constructorId`: Collega alla scuderia in `constructors`.
* `number`: Numero di vettura usato in quella gara.
* `grid`: Posizione di partenza in griglia.
* `position`: Posizione finale al traguardo (numerica).
* `positionText`: Posizione finale testuale (es. "1", "R" per ritirato).
* `positionOrder`: Campo numerico per ordinare i piloti.
* `points`: Punti guadagnati in gara.
* `laps`: Numero di giri completati.
* `time`: Tempo totale di gara (formato testo).
* `milliseconds`: Tempo totale di gara in millisecondi.
* `fastestLap`: Numero del giro più veloce del pilota.
* `rank`: Classifica del suo "giro più veloce" rispetto agli altri.
* `fastestLapTime`: Tempo del suo giro più veloce.
* `fastestLapSpeed`: Velocità media durante il giro più veloce.
* `statusId`: Collega a `status` per spiegare il motivo del ritiro o lo stato finale.

#### `qualifying` (Qualifiche)
Risultati delle sessioni di qualifica.
* `qualifyId`: ID unico (chiave primaria).
* `raceId`, `driverId`, `constructorId`: ID per collegare il risultato.
* `number`: Numero di vettura.
* `position`: Posizione finale in qualifica.
* `q1`, `q2`, `q3`: Tempi registrati nelle tre sessioni di qualifica.

#### `pitStops` (Soste ai Box)
Registra ogni sosta ai box durante una gara.
* `raceId`, `driverId`: Identificano la sosta.
* `stop`: Numero progressivo della sosta per quel pilota (1°, 2°, ...).
* `lap`: Giro in cui è stata effettuata la sosta.
* `time`: Ora del giorno della sosta.
* `duration`: Durata della sosta (es. "23.567").
* `milliseconds`: Durata in millisecondi.

#### `lapTimes` (Tempi sul Giro)
Contiene il tempo di ogni singolo giro per ogni pilota.
* `raceId`, `driverId`, `lap`: Chiave primaria composita.
* `position`: Posizione del pilota al termine di quel giro.
* `time`: Tempo di quel giro.
* `milliseconds`: Tempo del giro in millisecondi.

---

### 4. Tabelle delle Classifiche (Dati Aggregati)

Tabelle con dati riassuntivi, come le classifiche di campionato.

#### `driverStandings` (Classifica Piloti)
Classifica del campionato piloti dopo una specifica gara.
* `driverStandingsId`: ID unico (chiave primaria).
* `raceId`: ID della gara **dopo la quale** questa classifica è valida.
* `driverId`: ID del pilota.
* `points`: Punteggio totale fino a quel momento.
* `position`: Posizione in campionato.
* `wins`: Numero di vittorie in stagione fino a quel momento.

#### `constructorStandings` (Classifica Costruttori)
Classifica del campionato costruttori dopo una specifica gara.
* `constructorStandingsId`: ID unico (chiave primaria).
* `raceId`: ID della gara dopo la quale la classifica è valida.
* `constructorId`: ID della scuderia.
* `points`: Punteggio totale della scuderia.
* `position`: Posizione in campionato.
* `wins`: Numero di vittorie della scuderia in stagione.

#### `constructorResults` (Risultati per Costruttore)
Aggrega i punti ottenuti da una scuderia in una singola gara.
* `constructorResultsId`: ID unico (chiave primaria).
* `raceId`: ID della gara.
* `constructorId`: ID della scuderia.
* `points`: Punti totali ottenuti dalla scuderia in quella gara.
* `status`: Campo testuale che potrebbe indicare uno stato aggregato.