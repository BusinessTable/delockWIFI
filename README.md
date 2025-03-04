# delockWIFI

**Testkonzept für die geänderte Anwendung mit Login-Mechanismus**

---

### Ziel des Tests

Das Ziel ist die Verifizierung der Funktionalität des Programms, einschließlich:

1. Der Login-Funktion mit passwortgeschütztem Zugriff.
2. Der korrekten Speicherung und Anzeige der Geräte.
3. Der Steuerungsbefehle (Ein/Aus) für die Delock WLAN Power Socket Switch.

---

### Voraussetzungen

1. **Netzwerkverbindung**:
   - Das Delock WLAN Power Socket Switch ist im selben Netzwerk wie der Testcomputer.
   - Die IP-Adresse des Delock-Geräts wurde bereits ermittelt.

2. **Hardware**:
   - Ein Delock WLAN Power Socket Switch.
   - Ein Testgerät (z. B. eine Lampe), das mit dem Schalter verbunden ist.

3. **Software**:
   - Das Programm läuft auf dem Testcomputer.
   - Der Browser ist geöffnet, und die Login-Seite (`http://localhost:5000/login`) ist zugänglich.

4. **Zugriffsrechte**:
   - Eine `.env`-Datei mit der Umgebungsvariable `PASSWORD` (z. B. `PASSWORD=your_password`) ist eingerichtet. Siehe `example.env`

---

### Testaufbau

1. **Initialisierung**:
   - Starten Sie die Anwendung und navigieren Sie zur Login-Seite (`http://localhost:5000/login`).
   - Überprüfen Sie, ob die Login-Seite korrekt geladen wird.

2. **Login-Prüfung**:
   - Geben Sie das Passwort ein, das in der `.env`-Datei definiert ist.
   - Überprüfen Sie, ob Sie nach der Eingabe des korrekten Passworts auf die Hauptseite weitergeleitet werden.
   - Testen Sie ein falsches Passwort und überprüfen Sie, ob eine Fehlermeldung erscheint.

3. **Geräteverwaltung**:
   - Fügen Sie Geräte hinzu, prüfen Sie deren Speicherung und Darstellung nach einem Seitenneuladen.

---

### Testfälle

#### **Testfall 1: Login-Funktionalität**

1. Rufen Sie die Login-Seite auf.
2. Geben Sie das korrekte Passwort ein und bestätigen Sie.
3. **Erwartetes Ergebnis**: Weiterleitung zur Hauptseite mit der Geräteübersicht.
4. Geben Sie ein falsches Passwort ein.
5. **Erwartetes Ergebnis**: Fehlermeldung „Invalid password. Please try again“.

#### **Testfall 2: Geräte hinzufügen**

1. Melden Sie sich an und fügen Sie ein neues Gerät hinzu (Name: `Testgerät`, IP: `192.168.1.x`).
2. **Erwartetes Ergebnis**: Das Gerät wird in der Liste angezeigt, Status „Unknown“.
3. Laden Sie die Seite neu.
4. **Erwartetes Ergebnis**: Das Gerät bleibt in der Liste erhalten.

#### **Testfall 3: Gerät steuern**

1. Drücken Sie „Turn On“ für das hinzugefügte Gerät.
2. **Erwartetes Ergebnis**: Die Lampe leuchtet, Status: „On“.
3. Drücken Sie „Turn Off“.
4. **Erwartetes Ergebnis**: Die Lampe erlischt, Status: „Off“.

#### **Testfall 4: Mehrere Geräte**

1. Fügen Sie mehrere Geräte mit unterschiedlichen Namen und IP-Adressen hinzu.
2. **Erwartetes Ergebnis**: Alle Geräte werden korrekt in der Liste angezeigt und bleiben nach einem Seitenneuladen gespeichert.

#### **Testfall 5: Logout und erneuter Login**

1. Schließen Sie den Browser und öffnen Sie die Seite erneut.
2. **Erwartetes Ergebnis**: Sie werden auf die Login-Seite weitergeleitet.
3. Melden Sie sich erneut an.
4. **Erwartetes Ergebnis**: Die Geräteübersicht wird mit den gespeicherten Geräten geladen.

---

### Erfolgskriterien

- Der Login funktioniert nur mit dem korrekten Passwort.
- Geräte können hinzugefügt, gespeichert und korrekt angezeigt werden.
- Die Steuerungsbefehle (Ein/Aus) funktionieren zuverlässig.
- Nach einem Seitenneuladen oder Serverneustart bleiben die Geräte gespeichert.
- Mehrere Geräte können gleichzeitig verwaltet werden.

---

### Dokumentation

Ergebnisse der Tests werden in folgender Tabelle dokumentiert:

| Testfall                  | Erwartetes Ergebnis                             | Tatsächliches Ergebnis | Status    |
|---------------------------|------------------------------------------------|------------------------|-----------|
| Login-Funktionalität      | Weiterleitung zur Hauptseite                   | Bestanden             | ✅         |
| Geräte hinzufügen         | Gerät wird in der Liste angezeigt             | Bestanden             | ✅         |
| Gerät steuern (Ein/Aus)   | Status wird korrekt aktualisiert               | Bestanden             | ✅         |
| Mehrere Geräte hinzufügen | Alle Geräte werden korrekt verwaltet          | Bestanden             | ✅         |
| Logout und erneuter Login | Geräteübersicht wird nach Login angezeigt      | Bestanden             | ✅         |

Dieses Konzept stellt sicher, dass alle relevanten Funktionen umfassend getestet werden.
