open System

let rec fibonacci n =
    if n <= 1 then n
    else fibonacci (n - 1) + fibonacci (n - 2)

let rec fibonacciTailRec n a b =
    if n = 0 then a
    elif n = 1 then b
    else fibonacciTailRec (n - 1) b (a + b)

let zadanie1 () =
    let n = 10 // Przykładowa wartość n
    let wynik = fibonacci n
    let wynikOpt = fibonacciTailRec n 0 1
    printfn "n-ty wyraz ciągu Fibonacciego (rekurencyjnie): %d" wynik
    printfn "n-ty wyraz ciągu Fibonacciego (ogonowa rekurencja): %d" wynikOpt

[<EntryPoint>]
let main argv =
    zadanie1()

    printfn "Naciśnij dowolny klawisz, aby zakończyć..."
    Console.ReadKey() |> ignore
    0