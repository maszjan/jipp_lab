open System

type DaneUzytkownika = {
    Waga: float
    Wzrost: float
}

let obliczBMI (waga: float) (wzrost: float) : float =
    waga / ((wzrost / 100.0) ** 2.0)

let okreslKategorieBMI (bmi: float) : string =
    if bmi < 18.5 then "Niedowaga"
    elif bmi < 24.9 then "Waga prawidłowa"
    elif bmi < 29.9 then "Nadwaga"
    else "Otyłość"

let zadanie1 () =
    printfn "Podaj swoją wagę w kg: "
    let wagaInput = Console.ReadLine()
    printfn "Podaj swój wzrost w cm: "
    let wzrostInput = Console.ReadLine()

    let waga = float wagaInput
    let wzrost = float wzrostInput

    let daneUzytkownika = { Waga = waga; Wzrost = wzrost }

    let bmi = obliczBMI daneUzytkownika.Waga daneUzytkownika.Wzrost

    let kategoria = okreslKategorieBMI bmi

    printfn "Twoje BMI wynosi: %.2f" bmi
    printfn "Kategoria BMI: %s" kategoria

let zadanie2 () =
    let kursyWymiany = Map.ofList [("USD", 1.0); ("EUR", 0.85); ("GBP", 0.75)]

    printfn "Podaj kwotę do przeliczenia: "
    let kwotaInput = Console.ReadLine()
    printfn "Podaj walutę źródłową (USD, EUR, GBP): "
    let walutaZrodlowa = Console.ReadLine().ToUpper()
    printfn "Podaj walutę docelową (USD, EUR, GBP): "
    let walutaDocelowa = Console.ReadLine().ToUpper()

    let kwota = float kwotaInput

    if kursyWymiany.ContainsKey(walutaZrodlowa) && kursyWymiany.ContainsKey(walutaDocelowa) then
        let kursZrodlowy = kursyWymiany.[walutaZrodlowa]
        let kursDocelowy = kursyWymiany.[walutaDocelowa]
        let przeliczonaKwota = kwota * (kursDocelowy / kursZrodlowy)
        printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDocelowa
    else
        printfn "Nieprawidłowa waluta."

let zadanie3 () =
    printfn "Podaj tekst do analizy: "
    let tekst = Console.ReadLine()

    let slowa = tekst.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    let liczbaSlow = slowa.Length
    let liczbaZnakow = tekst.Replace(" ", "").Length

    let slowaMap = 
        slowa 
        |> Array.fold (fun acc slowo -> 
            if Map.containsKey slowo acc then 
                Map.add slowo (acc.[slowo] + 1) acc 
            else 
                Map.add slowo 1 acc) Map.empty

    let najczestszeSlowo = 
        slowaMap 
        |> Map.toList 
        |> List.maxBy snd 
        |> fst

    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakow
    printfn "Najczęściej występujące słowo: %s" najczestszeSlowo

[<EntryPoint>]
let main argv =
    printfn "Wybierz zadanie do wykonania:"
    printfn "1. Obliczanie BMI"
    printfn "2. Konwersja walut"
    printfn "3. Analiza tekstu"
    let wybor = Console.ReadLine()

    match wybor with
    | "1" -> zadanie1()
    | "2" -> zadanie2()
    | "3" -> zadanie3()
    | _ -> printfn "Nieprawidłowy wybór."

    0 