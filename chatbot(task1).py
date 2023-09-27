import re


# Define predefined rules and responses
rules = {
    r'hello|hi|hey': 'Hello! How can I assist you today?',

    r'how are you': 'I am just a chatbot, but I am here to help you!',
   
 r'what is your name|who are you': 'I am a simple chatbot.',
    
r'bye|goodbye': 'Goodbye! Have a great day!',
    
r'\b(?:thank you|thanks)\b': 'You\'re welcome!',
    
r'\b(?:help|what can you do)\b': 'I can provide information and answer questions. Just ask!',
   
 r'\b(?:weather|forecast)\b': 'I do not have access to real-time data, but I can help you find weather information online.',
}


# Function to respond to user input
def chatbot_response(user_input):
   
 for pattern, response in rules.items():
       
 if re.search(pattern, user_input, re.IGNORECASE):
           
 return response
   
 return "I'm sorry, I don't understand that."

#
 Main interaction loop
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")


while True:
   
 user_input = input("You: ")
    if user_input.lower() == 'bye':
     
   print("Chatbot: Goodbye! Have a great day!")
      
  break
   
 response = chatbot_response(user_input)
  
  print("Chatbot:", response)