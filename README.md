## Uitvoering

### 1. Database maken

Ik heb een SQLite-database gemaakt met de naam `database.db`.

In de database heb ik een tabel `users` gemaakt. Deze tabel bevat:

- `id` - uniek nummer van de gebruiker.
- `name` - naam van de gebruiker.
- `email` - e-mailadres van de gebruiker.

De `id` wordt automatisch aangemaakt met `AUTOINCREMENT`.

### 2. Projectstructuur

Ik heb een duidelijke projectstructuur gemaakt met verschillende mappen en bestanden:

- `app.py` - de Flask-applicatie.
- `database.py` - maakt de database en tabel aan.
- `templates/` - bevat de HTML-pagina's.
- `models/` - voor database-gerelateerde onderdelen.
- `routes/` - voor routes van de applicatie.
- `tests/` - voor testen.
- `database.db` - de SQLite-database.

### 3. Loginpagina

Ik heb een eenvoudige loginpagina gemaakt met velden voor een gebruikersnaam en wachtwoord.

### 4. Registratiepagina

Ik heb een registratiepagina gemaakt met velden voor:

- Gebruikersnaam
- E-mail
- Wachtwoord

De registratie wordt via Flask verwerkt.

### 5. Database koppelen

Ik heb Flask gekoppeld aan de SQLite-database met Python en `sqlite3`.

Wanneer een gebruiker zich registreert, worden de naam en het e-mailadres opgeslagen in de tabel `users`.

### 6. Gegevens toevoegen

Ik heb de registratie getest met testgegevens. De gegevens werden succesvol opgeslagen in de database.

### 7. Testen en fouten oplossen

Ik heb de applicatie getest door:

- De registratiepagina te openen.
- Een testregistratie te maken.
- Te controleren of de gegevens in de database stonden.
- Eventuele problemen met Flask en de database op te lossen.

De database gaf na het testen de opgeslagen gebruikersgegevens terug. Hierdoor kon ik controleren dat het opslaan van gegevens werkte.

## Resultaat

Het eindresultaat is een werkende Flask-webapplicatie die verbinding maakt met een SQLite-database.

De gebruiker kan een registratieformulier invullen en de gegevens worden vervolgens opgeslagen in de database.

## Conclusie

Door deze opdracht heb ik geleerd hoe ik een SQLite-database kan maken en hoe ik deze kan gebruiken in een Python Flask-applicatie.

Ik heb ook geleerd hoe ik gegevens kan opslaan met SQL, hoe ik een project kan testen en hoe ik problemen kan oplossen.

Daarnaast heb ik geoefend met Git, GitHub en het maken van een goede projectstructuur.