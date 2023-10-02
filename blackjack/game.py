from deck import Deck 
from player import UserPlayer, Dealer, Hand 

class Game:
    
    def __init__(self, starting_bet:int = 10):
        self._deck = Deck() 
        self._starting_bet = starting_bet
        while (user_money := int(input(f"Type in how much money you want to deposit: "))) < starting_bet:
            print(f"You have to deposit more than {starting_bet}")
        self._user = UserPlayer(Hand(), user_money)
        self._dealer = Dealer(Hand())
        
    
    def play_round(self):
        
        for _ in range(2):
            card = self._deck.draw()
            self._user.add_card(card)
            
            card = self._deck.draw() 
            self._dealer.add_card(card)
        
        print(f"user: {self._user.get_hand().get_cards()} \n")
        print(f"dealer: {self._dealer.get_hand().get_cards()[0]}, X \n")
        
        self._user.bet_money(self._starting_bet)
        winning_money = self._starting_bet
        
        while self._user.make_move():
            print("User Draw: \n")
            bet_money = int(input(f"Bet money. {1}-{self._user.get_money()}: "))
            self._user.bet_money(bet_money)
            winning_money += bet_money
            card = self._deck.draw() 
            self._user.add_card(card)
            if self._user.get_hand().get_score() > 21: 
                print(f"User score is over 21. You lose! Your current balance is {self._user.get_money()}")
                self.reset_game()
                return 
            else:
                print(f"User score is {self._user.get_hand().get_score()}")
        
        while self._dealer.make_move():
            print("Dealer Draw: \n")
            card = self._deck.draw() 
            self._dealer.add_card(card)
            if self._dealer.get_hand().get_score() > 21:
                self._user.add_money(winning_money * 2)
                print(f"Dealer score is over 21. You win! Your current balance is {self._user.get_money()}")
                self.reset_game()
                return 
            else:
                print(f"Dealer score is {self._dealer.get_hand().get_score()}")
        
        user_score = self._user.get_hand().get_score() 
        dealer_score = self._dealer.get_hand().get_score() 
        print(f"user score: {user_score}, dealer_score: {dealer_score} \n")
        if user_score > dealer_score:
            self._user.add_money(winning_money * 2)
            print(f"You win! Your current balance is {self._user.get_money()}")
        elif user_score < dealer_score:
            print(f"You lose! Your current balance is {self._user.get_money()}")
        else:
            self._user.add_money(winning_money)
            print(f"You draw! Your current balance is {self._user.get_money()}")
        self.reset_game()
        return 
    
    def reset_game(self):
        if self._user.get_money() < self._starting_bet:
            print(f"Your money is below the minimum bet. The game is over.")
            return 
        if input("Start new round? y/n: ") != "y":
            print("Finish the game!")
            return 
            
        self._deck = Deck()
        self._user.clear_hand()
        self._dealer.clear_hand()
        self.play_round()  
        