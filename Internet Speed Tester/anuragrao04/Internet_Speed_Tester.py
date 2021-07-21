import speedtest
# pip install speedtest

print("\n \nTesting...")
st = speedtest.Speedtest()

print("Download Speed: ", st.download()/1000000, "Mb/s")

print("Upload Speed: ", st.upload()/1000000, "Mb/s")

servernames = []
st.get_servers(servernames)
print("Ping Speed: ", st.results.ping, "ms")