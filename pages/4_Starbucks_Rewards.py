
################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################

# Starbucks Exchange List

# Database of Starbucks Exchange items including their name, digital address, rating and hourly cost per Ether.
gift_database = {
    "Bean": ["Coffee Bean - Medium Roast ", "0xaC8eB8B2ed5C4dhb328a84Ee4950F417f67029F0", "2.0", 300, "Images/s_bean.jpg"],
    "Drink": ["Peppermint Mocha", "0x2422858F9C4480c2dn23nb9D58Ffd7Ac8bF65396", "1.0", 50, "Images/s_drink.jpg"],
    "Gift Card": ["Starbucks Gift Card $25", "0x8fD00f170FDfdb329h1bdCD90bF257316c69BA45", "3.0", 250, "Images/s_giftcard.jpg"],
    "Tumbler": ["Gold Studded Tumbler", "0x8fD00f1KN32H3772C5ebdCD90bF257316c69BA45", "4.0", 600, "Images/s_tumbler.jpg"]
}

# A list of the gifts
gift = ["Bean", "Drink", "Gift Card", "Tumbler"]


def get_gift(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(gift_database.values())

    for number in range(len(gift)):
        image = db_list[number][4]
        st.image(image, width = 200)
        st.write("Name: ", db_list[number][0])
        st.write("Gift Address: ", db_list[number][1])
        st.write("Value Rating: ", db_list[number][2])
        st.write("Starbucks Reward Point per gift: ", db_list[number][3], "STRB")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Starbucks Reward List")
st.markdown("## Exchange Reward With Starbucks Token")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

#st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO: 
#  Call the `generate_account` function and save it as the variable `account`
#account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
#st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
#balance = get_balance(w3, account.address)
#st.sidebar.write(balance)

##########################################

# Create a select box to chose a FinTech Hire candidate
gift = st.sidebar.selectbox('Select a Gift', gift)

# Create a input field to record the number of hours the candidate worked
quantity = st.sidebar.number_input("Number of gift")

st.sidebar.markdown("## Gift, Reward Points, and Reward Address")

# Identify the FinTech Hire candidate
reward = gift_database[gift][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(reward)

# Identify the FinTech Finder candidate's hourly rate
rate = gift_database[gift][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(rate)

# Identify the FinTech Finder candidate's Ethereum Address
gift_address = gift_database[gift][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(gift_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Starbucks Reward Points")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:

# 1. Fintech Finder customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker. Code the application so that once a customer
# completes these steps, the application will calculate the amount that the
# worker will be paid in ether. To do so, complete the following steps:

    # * Write the equation that calculates the candidate’s wage. This equation
    #  should assess the candidate’s hourly rate from the candidate database
    # (`candidate_database[person][3]`) and then multiply this hourly rate by
    # the value of the `hours` variable. Save this calculation’s output as a
    # variable named `wage`.

    # * Write the `wage` variable to the Streamlit sidebar by
    # using `st.sidebar.write`.

# 2. Now that the application can calculate a candidate’s wage, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the hired candidate. To accomplish this, locate the
# code that reads `if st.sidebar.button("Send Transaction")`. You’ll need to
# add logic to this `if` statement that sends the appropriate information to
# the `send_transaction` function (which you imported from the `crypto_wallet`
# script file). Inside the `if` statement, add the following functionality:

    # * Call the `send_transaction()` function and pass it three parameters:
        # - Your Ethereum `account` information. (Remember that this `account`
        # instance was created when the `generate_account` function was called.)
        #  From the `account` instance, the application will be able to access the
        #  `account.address` information that is needed to populate the `from` data
        # attribute in the raw transaction.
        #- The `candidate_address` (which will be created and identified in the
        # sidebar when a customer selects a candidate). This will populate the `to`
        # data attribute in the raw transaction.
        # - The `wage` value. This will be passed to the `toWei` function to
        # determine the wei value of the payment in the raw transaction.

    # * Save the transaction hash that the `send_transaction` function returns
    # as a variable named `transaction_hash`, and have it display on the
    # application’s web interface.

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# @TODO
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
price = gift_database[gift][3] * quantity

# @TODO
# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(price)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


#if st.sidebar.button("Send Transaction"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    #transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    #st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
   #st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    #st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_gift(w3)

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run fintech_finder.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
    # * Take a screenshot of the address, balance, and transaction (TX) count.
    # Save this screenshot to the README.md file of your GitHub repository for
    #  this Challenge assignment.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
    # * Click the transaction and take a screenshot of it.
    # Save this screenshot to the README.md file of your GitHub repository for
    #  this Challenge assignment.
