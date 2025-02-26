# Meilleures pratiques en matière d'exceptions

Ne capturez pas les exceptions. Échoue rapidement et fortement. Si c'est important, quelqu'un d'autre s'occupera du problème. Capturez une exception seulement si vous êtes _celui-là_. C'est-à-dire, capturez seulement les erreurs où vous pouvez récupérer et continuer de manière raisonnable.
