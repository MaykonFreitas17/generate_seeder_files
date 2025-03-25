<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class {{TABELA_CAPITALIZADA}} extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        DB::table('{{TABELA}}')->delete();
        DB::table('{{TABELA}}')->insert([
            {{DADOS}}
        ]);
    }
}
