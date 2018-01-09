# -*- coding: utf-8 -*-
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

text = """
The Jacobins originated as the Club Breton at Versailles, where the deputies from Brittany to the Estates-General (later the National Assembly) of 1789 met with deputies from other parts of France to concert their action. The group was reconstituted, probably in December 1789, after the National Assembly moved to Paris, under the name of Society of the Friends of the Constitution, but it was commonly called the Jacobin Club because its sessions were held in a former convent of the Dominicans, who were known in Paris as Jacobins. Its purpose was to protect the gains of the Revolution against a possible aristocratic reaction. The club soon admitted nondeputies—usually prosperous bourgeois and men of letters—and acquired affiliates throughout France. By July 1790 there were about 1,200 members in the Parisian club and 152 affiliate clubs.
In July 1791 the Jacobin Club split over a petition calling for the removal of Louis XVI after his unsuccessful attempt to flee France; many of the moderate deputies left to join the rival club of the Feuillants. Maximilien Robespierre was one of the few deputies who remained, and he assumed a position of prominence in the club.

After the overthrow of the monarchy, in August 1792 (in which the Jacobin Club, still reluctant to declare itself republican, did not have a direct role), the club entered a new phase as one of the major groups directing the Revolution. With the proclamation of the republic in September, the club changed its name to Society of the Jacobins, Friends of Liberty and Equality. It acquired a democratic character with the admission of the leftist Montagnard deputies in the National Convention (the new legislature) and also a more popular one as it responded to the demands of the Parisian working and artisan class. Through the early phase of the Convention, the club was a meeting place for the Montagnards, and it agitated for the execution of the king (January 1793) and for the overthrow of the moderate Girondins (June 1793).

With the establishment of the Revolutionary dictatorship, beginning in the summer of 1793, the local Jacobin clubs became instruments of the Reign of Terror. (In 1793 there were probably 5,000 to 8,000 clubs throughout France, with a nominal membership of 500,000.) The clubs, as part of the administrative machinery of government, had certain duties: they raised supplies for the army and policed local markets. Often local government officials were replaced with members of clubs. As centres of public virtue, the clubs watched over people whose opinions were suspect, led the dechristianizing movement, and organized Revolutionary festivals.

The Parisian club was increasingly associated with Robespierre, who dominated the Revolutionary government through his position on the Committee of Public Safety. It supported Robespierre in his attacks on the enemies of the Revolution and helped him resist the growing demands of the discontented workers for a controlled economy. After the fall of Robespierre on 9 Thermidor, year II (July 27, 1794), the Parisian club, now a symbol of dictatorship and terror, was temporarily closed. It reopened as a centre of opposition to the Thermidorian government, but it was permanently closed on 21 Brumaire, year III (November 11, 1794).

The Club du Panthéon in 1795 and Club du Manège of 1799 briefly revived the Jacobin spirit, while some local clubs lasted until the year VIII (1799–1800) despite their having been officially banned.

The name Jacobin was also applied to radicals in England and other countries in the period of the French Revolution.
"""

print summarize(text)
