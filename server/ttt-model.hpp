#include <vector>
#include <iostream>

using namespace std;

class TicTacToeBoard
{
    public:

        enum class Player: char
        { 
            X, 
            O,
        };

        class BoardTile
        {
            bool _in_use;
            Player _player;

            public:

                bool operator==(const BoardTile& other)
                {
                    return _in_use == other._in_use &&
                           _player == other._player;
                }

                bool is_in_use()
                {
                    return _in_use;
                }

                void mark(const Player& player)
                {
                    _in_use = true;
                    _player = player;
                }
        };

        enum class PlayResult 
        {
            NEXT_TURN,
            WINNER,
            DRAW,
            INVALID_PLAY
        };

        std::vector<std::vector<BoardTile>> _board;

        TicTacToeBoard(): 
            _board(3, std::vector<BoardTile>(3, BoardTile())),
            _player_in_turn(Player::X)
        {
        }

        Player next_player()
        {
            return _player_in_turn;
        }

        PlayResult play(const Player& player, const int x, const int y)
        {
            if(_board[x][y].is_in_use())
                return PlayResult::INVALID_PLAY;

            if(_player_in_turn != player)
                return PlayResult::INVALID_PLAY;

            _board[x][y].mark(player);

            if(_player_in_turn == Player::X)
                _player_in_turn = Player::O;
            else if(_player_in_turn == Player::O)
                _player_in_turn = Player::X;

            return _check_play_result();
        }

    private:
     
        Player _player_in_turn;

        PlayResult _check_play_result()
        {
            for(auto col_index = 0; col_index < _board.size(); col_index++)
            {
               if(_board[col_index][0].is_in_use() &&
                  _board[col_index][0] == _board[col_index][1] &&
                  _board[col_index][1] == _board[col_index][2])
                   return PlayResult::WINNER;
            }

            return PlayResult::NEXT_TURN;
        }
};
