# Shorty - Générateur de raccourcis bureau

Shorty est un petit programme permettant de créer un raccourci sur un bureau Linux et Windows. Il a été conçu dans l'idée de rendre un peu plus accessible la création d'un raccourci sur un bureau Linux, en plus d'être un exercice pratique pour moi.

## Fonctionnement général

Le programme permet de choisir le nom du raccourci ainsi que l'exécutable cible.

### Linux

Sur un système Linux, une vérification de l'existence du dossier `~/.local/share/applications` se fait, et il est créé s'il n'existe pas ou nest pas trouvé. Lors de la création du raccourci sur le bureau, on peut choisir de l'ajouter également dans la liste des applications. (Testé sous Debian 13 avec GNOME et Arch Linux avec XFCE)

Il est possible de définir une icône personnalisée.

### Windows

Sur un système Windows, il n'est pas possible de choisir l'icône. S'il est déjà possible de créer un raccourci en ouvrant le menu contextuel sur un fichier, c'était un petit challenge pour ma part d'adapter le code pour qu'il soit exécuté sur Windows comme sur Linux.

## Pistes d'améliorations

- Permettre la génération de raccourcis pour des fichiers qui ne sont pas des ".AppImage", ".sh" ou autres ".exe"
- Ajouter un brin de couleur aux textes
- Rendre l'interface moins terne