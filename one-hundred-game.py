n = 5
gameboard = ['' for i in range(n**2)]

def isFinished(board):
 for i in range(len(board)):
  if board[i] == '':
   return False
 return True


def findIntoBoard(board, indx):
 for i in range(len(board)):
  if board[i] == indx:
   return i
    
def getAvailablePositions(board, indx):
 if indx == 1:
  return [i for i in range(len(board))]
 else:
  curr = findIntoBoard(board, indx-1)
  result = []
  # three cells up
  if curr/n > 2:
   result.append(curr-(n*3))
  
  # three cells down
  if curr/n < n-3:
   result.append(curr+(n*3))
   
  # three cells left
  if curr%n > 2:
   result.append(curr-3)
   
  if curr%n >= 2:
   if curr/n > 1:
    # 2 cells up, 2 cells left
    result.append(curr-2-(n*2))
   if curr/n < n-2:
    # 2 cells down, 2 cells left
    result.append(curr-2+(n*2))
    
  # three cells right
  if curr%n < n-3:
   result.append(curr+3)
   
  if curr%n <= n-3:
   if curr/n > 1:
    # 2 cells up, 2 cells right
    result.append(curr+2-(n*2))
   if curr/n < n-2:
    # 2 cells down, 2 cells right
    result.append(curr+2+(n*2))
  
  return filter(lambda pos: board[pos] == '' and pos >= 0 , result)

def resolveGame(board, indx = 1):
 if isFinished(board):
  print(board)
  return True
 else:
  availablePositions = getAvailablePositions(board, indx)
  for pos in availablePositions:
   board[pos] = indx
   if resolveGame(board, indx+1):
    return True
   board[pos] = ''
  return False

resolveGame(gameboard)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    