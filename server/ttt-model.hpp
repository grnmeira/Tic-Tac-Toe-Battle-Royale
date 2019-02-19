

class TicTacToeBoard
{
    public:

        enum class Player { X, O };

        Player next_player()
        {
            return Player::X;
        }

    private:
     
        Player _player_in_turn;
};
