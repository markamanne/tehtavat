def main():
    sanat = ["hitto", "hattu", "kissa", "matto", "talo", "appelsiini"]
    yli_viisi_kirjainta = 0

    for sana in sanat:
        if len(sana) > 5:
            yli_viisi_kirjainta += 1
            print(f"Löytyi pitkä sana: {sana} ({len(sana)} kirjainta)")
    print(f"\nListassa oli yhteensä {yli_viisi_kirjainta} sanaa, joissa on yli 5 kirjainta.")
if __name__ == "__main__":
    main()