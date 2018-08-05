package com.example.karthik.smart_community_system

import android.content.Intent
import android.net.Uri
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val people_in = findViewById<TextView>(R.id.people_in)
        val people_out = findViewById<TextView>(R.id.people_out)
        val total_people = findViewById<TextView>(R.id.total_people)
        val time_in = findViewById<TextView>(R.id.time_in)
        val time_out = findViewById<TextView>(R.id.time_out)

        val myThread = Thread ( Runnable {
            run {
                while (true) {
                    Thread.sleep(5000)
                    MyTask(total_people, people_in, time_in, people_out, time_out).execute()
                }
            }
        })

        myThread.start()

        val button = findViewById<Button>(R.id.button)

        button.setOnClickListener {
            val uri = Uri.parse("http://192.168.1.5/community_db.php") //Apache Server
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }
    }
}