
Bibliotekssystem i Python – README

Dette projekt er et simpelt og interaktivt bibliotekssystem skrevet i Python. Det giver mulighed for at administrere bøger og medlemmer, og understøtter udlån og returnering af bøger via en tekstbaseret menu.



Kodeoversigt

1. Book-klassen
Repræsenterer en bog i biblioteket.

- Attributter:
  - book_id: Unikt numerisk ID for bogen.
  - title: Bogens titel.
  - author: Navn på forfatteren.
  - copies: Antal tilgængelige eksemplarer.

- Metoder:
  - display_info(): Returnerer en streng med bogens oplysninger, f.eks. ID, titel og antal eksemplarer.
  - update_book(title, author, copies): Bruges til at opdatere bogens oplysninger. Man kan vælge kun at ændre enkelte felter.



2. Member-klassen
Repræsenterer et bibliotekets medlem.

- Attributter:
  - member_id: Unikt numerisk ID.
  - name: Medlemmets navn.
  - password: Adgangskode til sikkerhedsverificering.
  - borrowed_books: En liste over de bøger, medlemmet har lånt.

- Metoder:
  - verify_password(): Anmoder brugeren om at indtaste adgangskoden og returnerer True eller False.
  - display_info(): Viser medlemsdata og en liste over lånte bøger.
  - borrow_books(books): Modtager en liste af bøger og forsøger at låne dem. Hvis eksemplarer ikke er tilgængelige, får brugeren besked.
  - return_books(books): Modtager en liste af bøger og returnerer dem, hvis de findes i medlemmets låneliste.


3. Library-klassen
Håndterer den overordnede drift og organisering af bøger og medlemmer.

- Attributter:
  - books: En liste over alle Book-objekter i systemet.
  - members: En liste over alle Member-objekter.

- Metoder:
  - add_book(book): Tilføjer en bog til biblioteket.
  - remove_book(book_id): Fjerner en bog ud fra dens ID.
  - add_member(member): Tilføjer en ny bruger.
  - remove_member(member_id): Fjerner et medlem baseret på ID.
  - choose_action(member_id): Bruges til at låne eller returnere bøger efter adgangskodevalidering.
  - issue_books(member): Gennemfører udlån efter brugerinput.
  - return_books(member): Gennemfører returnering efter brugerinput.
  - display_books(): Returnerer en liste med oplysninger om alle bøger.
  - display_members(): Returnerer en liste med oplysninger om alle medlemmer.
  - run(): Hovedloopet for programmet. Viser menu og styrer navigationen.

Adgangskodebeskyttelse

Når et medlem skal låne eller returnere bøger, skal vedkommende først indtaste sin adgangskode korrekt. Hvis adgangskoden er forkert, får brugeren besked, og handlingen bliver afbrudt. Dette sikrer, at kun rette personer kan ændre på deres lånestatus.


Hvordan foregår udlån og returnering?

- Når en bruger vælger at låne bøger:
  - Der vises en liste over alle tilgængelige bøger.
  - Brugeren indtaster ID'er eller titler på de bøger, de vil låne (komma-separeret).
  - Systemet reducerer antallet af kopier, og tilføjer bogen til brugerens låneliste.

- Når en bruger vælger at returnere bøger:
  - Der vises kun de bøger, som brugeren har lånt.
  - Brugeren angiver hvilke de vil returnere.
  - Systemet opdaterer beholdningen og fjerner bogen fra lånelisten.



Brugerinput og menu

Når programmet kører, mødes man med denne menu:


 Library Menu 
1. Display all books
2. Display all members
3. Add a book
4. Remove a book
5. Add a member
6. Remove a member
7. Member actions (borrow/return)
8. Exit


Alle valg foretages via indtastning af tal (1-8).

Eksempel på tilføjelse af bog:

Enter book ID: 4
Enter title: Artificial Intelligence
Enter author: Alan Turing
Enter number of copies: 2




Fejlhåndtering

- Fejlagtig indtastning (f.eks. bogstaver i stedet for tal) bliver fanget af try/except.
- Hvis en bog eller et medlem ikke findes, informeres brugeren om dette.
- Brugeren får altid mulighed for at prøve igen, indtil gyldigt input gives.


