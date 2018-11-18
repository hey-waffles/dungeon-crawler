import board as b
import screen


##
# The main method. Handles startup and board rendering
##
def main():
	board = b.Board(80,23);
	screen.render(board);

main() 