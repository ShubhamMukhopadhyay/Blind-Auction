# 🎯 Silent Auction Program
# ------------------------------------------------------------
# This program simulates a simple auction where multiple users
# can place bids. The highest bidder wins.
# ------------------------------------------------------------

# 🏛️ Import and display the ASCII gavel logo
import art
print(art.gavel_logo)

# 🧾 Dictionary to store bidders and their bid amounts
bids = {}

# 🥇 Function to find the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\n🏆 The winner is {winner} with a bid of ₹{highest_bid}!\n")

# 💡 Shortcut (alternative method)
# res = max(bids, key=bids.get)
# print(f"The winner is {res} with a bid of {bids[res]}")

# 🔁 Continue asking for new bids
should_continue = True
while should_continue:

    user_name = input("👤 What is your name? : ")
    bid_price = int(input("💰 What is your bid? : ₹"))
    bids[user_name] = bid_price

    continue_bid = input("📝 Are there any other bidders? Type 'yes' or 'no': ").lower()

    if continue_bid == "no":
        should_continue = False
        find_highest_bidder(bids)

    elif continue_bid == "yes":
        print("\n" * 200)  # Clears the screen (simulated)
