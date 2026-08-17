import random
import time

def play_advanced_tournament():
    print("=" * 60)
    print("🔒 ADVANCED CYBER-HEIST SIMULATION: THE N-PLAYER TOURNAMENT 🔒")
    print("=" * 60)
    
    try:
        n = int(input("Enter the total number of students (n): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if n < 3:
        print("⚠️ Warning: You need at least 3 players to award 1st, 2nd, and 3rd place!")
        return

    # Master list to save player attempts and stats
    leaderboard = []

    for i in range(1, n + 1):
        print(f"\n" + "-" * 40)
        print(f"👤 Operative {i} of {n} entering the simulation...")
        name = input("Enter operative codename/name: ")
        
        # Game Variables
        target_code = random.randint(1, 100)
        attempts = 0
        energy = 100  # Starting energy resource
        start_time = time.time()
        
        print(f"\n[SYSTEM ALERT]: Welcome, {name}. Crack code (1-100).")
        print(f"[STATUS]: Energy: {energy}% | Target Code: Encrypted")
        
        while energy > 0:
            # Random dynamic event happening mid-turn
            energy = 100
            if energy <= 0:
                print("💥 System depleted your energy. Hack failed!")
                break

            try:
                guess = int(input(f"-> Enter code guess (Energy left: {energy}%): "))
                attempts += 1
                energy -= 15  # Each guess costs energy
                
                if guess < target_code:
                    print("   └── Status: Code too LOW. 📉 (-15% Energy)")
                elif guess > target_code:
                    print("   └── Status: Code too HIGH. 📈 (-15% Energy)")
                else:
                    elapsed_time = round(time.time() - start_time, 2)
                    print(f"🎉 SUCCESS! {name} bypassed the vault in {attempts} attempts and {elapsed_time}s!")
                    
                    # Save structured data to our master list
                    leaderboard.append({
                        "name": name,
                        "score": attempts,
                        "energy_left": energy,
                        "time_taken": elapsed_time
                    })
                    break
            except ValueError:
                print("   └── [ERROR]: Invalid input format. Try a valid integer.")
        
        else:
            # Executes if the loop breaks because energy ran out
            print(f"❌ OUT OF ENERGY! {name} failed to crack the vault.")
            leaderboard.append({
                "name": name,
                "score": 999,  # Penalty score for failing
                "energy_left": 0,
                "time_taken": 999.0
            })

    # Sort logic: Primary key is lowest score (attempts), Secondary key is highest energy left, Tertiary key is fastest time
    leaderboard.sort(key=lambda x: (x["score"], -x["energy_left"], x["time_taken"]))

    # Announcing Results
    print("\n" + "=" * 60)
    print("🏆 FINAL HACKING TOURNAMENT LEADERBOARD 🏆")
    print("=" * 60)
    
    medals = ["🥇 1st Place Elite Hacker", "🥈 2nd Place Cyber Specialist", "🥉 3rd Place Network Operative"]
    
    for i in range(min(3, len(leaderboard))):
        p = leaderboard[i]
        if p["score"] == 999:
            print(f"{medals[i]}: {p['name']} - Failed to hack the system")
        else:
            print(f"{medals[i]}: {p['name']} | Attempts: {p['score']} | Energy Left: {p['energy_left']}% | Time: {p['time_taken']}s")


    if len(leaderboard) > 3:
        print("\n--- Remaining Operatives ---")
        for i in range(3, len(leaderboard)):
            p = leaderboard[i]
            print(f"{i + 1}. {p['name']} (Attempts: {p['score'] if p['score'] != 999 else 'Failed'})")
            
    print("=" * 60)


play_advanced_tournament()