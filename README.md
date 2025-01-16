# delockWIFI

**Testkonzept zur Verifizierung der Funktionalität des Programms**

---

### Ziel des Tests

Das Ziel des Tests ist es, zu überprüfen, ob das Programm korrekt mit dem Delock WLAN Power Socket Switch funktioniert, indem es die Steuerungsbefehle (Ein/Aus) über die IP-Adresse ausführt und der Status der Geräte korrekt angezeigt wird.

---

### Voraussetzungen

1. **Netzwerkverbindung**:
   - Das Delock WLAN Power Socket Switch muss mit demselben Netzwerk verbunden sein wie der Computer, auf dem das Programm ausgeführt wird.
   - Die IP-Adresse des Delock-Geräts wurde mit der App *Fing* ermittelt.

2. **Hardware**:
   - Ein Delock WLAN Power Socket Switch.
   - Ein Gerät (z. B. eine Lampe), das an den Delock-Schalter angeschlossen ist.

3. **Software**:
   - Das Programm läuft auf dem Testcomputer.
   - Ein Browser ist geöffnet, und die Benutzeroberfläche des Programms ist erreichbar (z. B. `http://localhost:5000`).

4. **Zugriffsrechte**:
   - Der Testcomputer hat Zugriff auf das lokale Netzwerk und kann HTTP-Anfragen an die Delock IP-Adresse senden.

---

### Testaufbau

1. **Initialisierung**:
   - Starten Sie das Programm und öffnen Sie die Benutzeroberfläche im Browser.
   - Vergewissern Sie sich, dass das Gerät über die IP-Adresse erreichbar ist, indem Sie die Adresse `http://<Delock-IP>/cm?cmnd=Power%20On` im Browser aufrufen.

2. **Eingabeprüfung**:
   - Fügen Sie in der Benutzeroberfläche ein neues Gerät mit dem Namen `Testgerät` und der zuvor ermittelten IP-Adresse hinzu.
   - Überprüfen Sie, ob das Gerät korrekt in der Liste der Geräte erscheint.

---

### Testfälle

#### **Testfall 1: Gerät ein- und ausschalten**

1. Drücken Sie in der Benutzeroberfläche auf "Turn On".
2. Beobachten Sie, ob das an den Delock angeschlossene Gerät eingeschaltet wird (z. B. die Lampe leuchtet).
3. Überprüfen Sie, ob der Status des Geräts in der Benutzeroberfläche auf "On" aktualisiert wird.
4. Drücken Sie auf "Turn Off".
5. Beobachten Sie, ob das an den Delock angeschlossene Gerät ausgeschaltet wird (z. B. die Lampe erlischt).
6. Überprüfen Sie, ob der Status des Geräts in der Benutzeroberfläche auf "Off" aktualisiert wird.

#### **Testfall 2: Fehlerhafte IP-Adresse**

1. Fügen Sie ein neues Gerät mit einer ungültigen oder falschen IP-Adresse hinzu.
2. Drücken Sie auf "Turn On" oder "Turn Off".
3. Überprüfen Sie, ob das Programm eine Fehlermeldung anzeigt (z. B. "Error controlling device").

#### **Testfall 3: Mehrere Geräte hinzufügen**

1. Fügen Sie mehrere Geräte mit verschiedenen Namen und IP-Adressen hinzu.
2. Testen Sie für jedes Gerät die Funktionen "Turn On" und "Turn Off".
3. Überprüfen Sie, ob die Statusanzeigen korrekt aktualisiert werden.

---

### Erfolgskriterien

- Geräte lassen sich zuverlässig ein- und ausschalten.
- Der Status jedes Geräts wird korrekt angezeigt.
- Fehlermeldungen werden für ungültige oder nicht erreichbare Geräte ausgegeben.
- Die Benutzeroberfläche bleibt stabil, auch wenn mehrere Geräte hinzugefügt werden.

---

### Dokumentation

Während der Tests werden die Ergebnisse in einer Tabelle dokumentiert:

| Testfall         | Erwartetes Ergebnis                           | Tatsächliches Ergebnis |
|------------------|-----------------------------------------------|------------------------|
| Gerät einschalten | Lampe leuchtet, Status: "On"                 | Bestanden    |
| Gerät ausschalten | Lampe erlischt, Status: "Off"                | Bestanden    |
| Fehlerhafte IP    | Fehlermeldung: "Device not reachable"         | Bestanden    |
| Mehrere Geräte    | Alle Geräte funktionieren wie erwartet        | Bestanden    |

---

Mit diesem Konzept können Sie systematisch prüfen, ob das Programm wie gewünscht funktioniert. Falls Fehler auftreten, können die Ergebnisse genutzt werden, um gezielt Verbesserungen vorzunehmen.
