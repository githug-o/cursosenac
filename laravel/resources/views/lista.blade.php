<html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body>
        <a href="{{route('inputs')}}"><button type="button" class="btn btn-primary">Criar</button></a>
        <table class="table table-striped">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Nome</th>
        <th scope="col">E-mail</th>
        <th scope="col">Telefone</th>
        <th scope="col">CEP</th>
        <th scope="col">Cidade</th>       
        <th scope="col">UF</th>
        <th scope="col">Rua</th>
        <th scope="col">Bairro</th>
        <th scope="col">Nº</th>
        <th scope="col">Complemento</th>
        </tr>
    </thead>    
    <tbody>
    @foreach ($cliente as $cliente)
        <tr>
        <th scope="row">{{$cliente->id}}</th>
        <td>{{$cliente->nome}}</td>
        <td>{{$cliente->email}}</td>
        <td>{{$cliente->telefone}}</td>
        <td>{{$cliente->cep}}</td>
        <td>{{$cliente->cidade}}</td>
        <td>{{$cliente->uf}}</td>
        <td>{{$cliente->rua}}</td>
        <td>{{$cliente->bairro}}</td>
        <td>{{$cliente->numero}}</td>
        <td>{{$cliente->complemento}}</td>
        <td>
            <div>
                <a href="{{route('editar', $cliente->id)}}"><button type="button" class="btn btn-warning">Editar</button></a>
                <a href="{{route('deletar', $cliente->id)}}"><button type="button" class="btn btn-danger">Excluir</button></a>               
            </div>
        </td>      

        </tr>
    @endforeach
    </tbody>
    </table>
    </body>
</html>
