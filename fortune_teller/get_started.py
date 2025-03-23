import sys
from fortune_teller.mood_fortune import mood_fortune
from fortune_teller.fortune_stories import fortune_story
from fortune_teller.cs_fortune import cs_fortune
from fortune_teller.date_time import rand_date_time

FORTUNE_COOKIE_ART = r"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠐⠒⠂⠀⠐⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⣀⣠⣄⡀⠀⠀⠀⠉⠂⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⡐⣡⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠰⢱⢟⠸⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡎⡿⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⢰⢱⡇⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣦⠀⠀⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠸⣼⠱⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⡄⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢨⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡄⠀⠀⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢨⡧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⡀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⢸⡇⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣧⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⣹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⠸⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣾⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡆⠀⠀⠀⠀⠀⣀⣀⣤⢤⣤⣀⣤⣤⣠⣄⣀⡀⠀⠀⠀⠀⠈⠁⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⠠⠀⠀⠈⠁⠀⠀⠀⠀⠀⣀⡀⠤⠤⠄⣒⣦⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⠤⠔⢊⣩⣴⡾⠿⠛⠋⠉⠉⠉⠉⠉⠉⠉⠙⠛⠓⠶⣤⣤⣀⠀⠀⠀⠁⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡀⠔⠉⠀⠀⠀⣀⠠⠤⠐⣒⣊⣭⣥⡶⠶⠶⠚⠛⠉⠁⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⣤⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣖⡤⡀⠀⠀⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡜⠁⠀⢀⡤⣒⣩⣤⠶⠞⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢾⣗⢄⡀⠀⠀⠐⢀⠀⠀⠀⠀⠀
⢠⠃⠀⢰⠏⢾⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢘⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣍⢢⡀⠀⠈⠢⠀⠀⠀⠀
⠈⡆⠀⠈⠙⡌⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣜⣄⠀⠀⠱⡀⠀⠀
⠀⠈⠢⠀⠀⠈⢌⡻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⣦⠀⠀⢱⠀⠀
⠀⠀⠀⠱⡀⠀⠀⠑⢽⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡀⠀⠀⢃⠀
⠀⠀⠀⠀⠈⠢⡀⠀⠀⠙⠯⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣼⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠘⡄
⠀⠀⠀⠀⠀⠀⠈⠒⣀⠀⠀⠉⠫⢿⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⡀⠀⠀⠈⠛⠹⢟⡳⠶⢦⣤⣤⣤⣤⣤⡴⠶⠛⢻⡉⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠀⠀⢠⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⢀⠀⠀⠀⠀⠉⠉⠈⠈⠁⠀⠀⠀⠀⠀⠀⠑⠤⣉⣛⣻⢿⠷⣷⢶⣶⣶⣦⣴⣦⣤⣤⣤⣀⡀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠇⠀⠀⡎⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠒⠂⠀⠀⠀⠀⠀⠀⠐⠀⠈⠢⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⢽⣻⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣫⠃⠀⠀⡜⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠐⠒⠒⠒⠂⠂⠀⠀⠀⠀⠀⠐⡂⠀⠀⢀⢪⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⢟⠝⠁⠀⢀⠜⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⢀⢃⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⣿⢟⡷⠁⠀⠀⡠⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⡨⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⡟⡯⠋⠀⠀⢀⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⣷⡏⡀⠀⡀⠀⠀⠀⠀⠀⣀⣀⣤⣴⡶⠟⡛⠉⠀⣿⣿⣿⡟⡻⠋⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠁⢠⠼⣴⢺⡄⠀⠘⢿⣏⠉⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⣿⣆⠉⠿⠿⡿⣿⣿⣿⢿⣇⠀⠀⠸⣷⢈⡿⠀⠀⠀⠀⠿⣷⡀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⠀⠀⠘⢍⠛⠾⠶⠶⠶⠶⠶⡶⢿⣆⠀⠀⠀⠙⠁⠀⣀⣤⣶⠾⠟⠋⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠻⣧⣄⣤⡶⠾⠛⠋⠉⠀⠀⠀⠀⣀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠂⠠⠤⠤⠀⠀⠀⠀⠄⠀⠀⠀⠁⠀⠀⠀⠀⠀⣀⠠⠀⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠂⠀⠀⠀⠀⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def print_fortune_in_cookie(fortune_text: str) -> None:
    print(FORTUNE_COOKIE_ART)
    print("cookie art taken from emojicombos website")
    print("Here's your fortune:")
    print("               ↓")
    print(f"  {fortune_text}\n")

def main():
    print("Welcome to the Fortune Teller!")
    print("Try your luck today with one of the following fortune functions:")
    print("  1) mood_fortune (receive fortunes based on your mood)")
    print("  2) fortune_story (receive personalized story fortunes)")
    print("  3) cs_fortune (receive fortunes based on a computer science topic)")
    print("  4) Quit")
    
    while True:
        choice = input("\nWhich fortune function would you like to use? type 1/2/3/4) ").strip()
        
        if choice == "1":
            handle_mood_fortune()
        elif choice == "2":
            handle_fortune_story()
        elif choice == "3":
            handle_cs_fortune()
        elif choice == "4":
            print("Goodbye for now but remember: luck waits for no one!")
            sys.exit(0)
        else:
            print("Oops, invalid choice. Please enter 1, 2, 3, or 4.")

def handle_mood_fortune():
    """
    Asks the user to pick a mood, gets a fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'mood_fortune'. Now, choose your mood: positive, funny, cursed, motivational.")
    mood = input("Enter your mood: ").strip()
    
    fortune = mood_fortune(mood)
    
    if fortune.startswith("Error:"):
        print(fortune)
        return
    
    print_fortune_in_cookie(fortune)
    
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, fortune)
        print_fortune_in_cookie(combined)

def handle_fortune_story():
    """
    Asks the user to provide a name, gets a story fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'fortune_story'.")
    name = input("For whom is this fortune? (enter your/their name): ").strip()
    
    story = fortune_story(name)
    
    if story.startswith("Error:"):
        print(story)
        return
    
    print_fortune_in_cookie(story)
    
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, story)
        print_fortune_in_cookie(combined)

def handle_cs_fortune():
    """
    Asks the user to pick a category, gets a CS fortune, and optionally combines it with a random date.
    """
    print("\nYou chose 'cs_fortune'. Now, please pick a category: tech, startup, open source, ai, career.")
    category = input("Enter your category: ").strip()
    
    cs_message = cs_fortune(category)
    
    if cs_message.startswith("Error:"):
        print(cs_message)
        return
    
    print_fortune_in_cookie(cs_message)
    
    add_date = input("\nWould you like to know when this fortune is going to happen?! (y/n) ").strip().lower()
    if add_date == "y":
        current_date_str = input("Please enter the current date (YYYY-MM-DD, year <= 2025): ").strip()
        combined = rand_date_time(current_date_str, cs_message)
        print_fortune_in_cookie(combined)

if __name__ == "__main__":
    main()
