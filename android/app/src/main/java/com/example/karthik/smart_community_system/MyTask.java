package com.example.karthik.smart_community_system;

import android.os.AsyncTask;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class MyTask extends AsyncTask <Void, Void, String> {
    TextView tv1, tv2, tv3, tv4, tv5;

    public MyTask(TextView tv1, TextView tv2, TextView tv3, TextView tv4, TextView tv5) {
        this.tv1 = tv1;
        this.tv2 = tv2;
        this.tv3 = tv3;
        this.tv4 = tv4;
        this.tv5 = tv5;
    }

    @Override
    protected String doInBackground(Void... voids) {

        String device = "[DEVICE_NAME]@[USERNAME].[USERNAME]";
        String returnMsg = "";
        String request = "https://api.carriots.com/streams/?order=-1&max=1";

        URL url;
        HttpURLConnection connection = null;

        try {
            url = new URL(request);

            Thread.sleep(500);
            connection = (HttpURLConnection) url.openConnection();

            connection.addRequestProperty("Carriots.apiKey", "[CARRIOTS_APIKEY]");
            connection.addRequestProperty("Accept-Type", "application/json");
            connection.setRequestMethod("GET");

            BufferedReader input = new BufferedReader(new InputStreamReader((InputStream) connection.getContent()));

            returnMsg += input.readLine();

            connection.disconnect();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ProtocolException e) {
            e.printStackTrace();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            connection.disconnect();
        }

        return returnMsg;
    }

    protected void onPostExecute(String returnMsg){
        try {
            JSONObject json = new JSONObject(returnMsg);
            JSONArray result = json.getJSONArray("result");
            JSONObject firstResult = result.getJSONObject(0);
            JSONObject data = firstResult.getJSONObject("data");

            final int total_people = data.getInt("count");
            final int people_in = data.getInt("entered");
            final String time_in = data.getString("time_of_entry");
            final int people_out = data.getInt("exited");
            final String time_out = data.getString("time_of_exit");

            tv1.setText(Integer.toString(total_people));
            tv2.setText(Integer.toString(people_in));
            tv3.setText(time_in);
            tv4.setText(Integer.toString(people_out));
            tv5.setText(time_out);

        } catch (JSONException e) {
            e.printStackTrace();
        }

    }
}